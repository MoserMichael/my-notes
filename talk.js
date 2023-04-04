const { Configuration, OpenAIApi } = require("openai");
const fs=require("node:fs");
const readline = require('readline-sync');


//
// openai API stuff:
//
const chatGPTApiKey="PUT YOUR OPENAI API KEY HERE";
const chatGPTOrgId="PUT YOUR OPENAI ORG ID HERE";


const configuration = new Configuration({
  organization: chatGPTOrgId,
  apiKey: chatGPTApiKey,
});

const openai = new OpenAIApi(configuration);
const debugIt = false;

//
// global state
// 
let conversation=[];
let max_token_value = 100;
let model_name = "text-davinci-003";
let temperature_value = -1;

//
// constants
// 
const set_max_token_cmd ="set-max-token ";
const set_temperature_cmd = "set-temperature "
const read_file_cmd = "read-file ";
const save_cmd = "save-file ";
const help_cmd = "help?";
const show_cmd = "show?";
const list_models_cmd = "list_models?";
const clear_cmd = "clear!";

const conversation_file_name = "conversation.txt";

// command handlers

function showHelp() {
    console.log(`
--------------
Commands
` + set_max_token_cmd + `<integer number>\t set maximum number of tokens consumed per createCompletion api call
` + set_temperature_cmd + `<float point>\t set the 'temperature'/'creativity' - 0.2 - creative , 0.8 - more 'focused' (must be between 0..2)
` + save_cmd + `<filename>\t\t save current state of conversation fo json file.
` + read_file_cmd + `<filename>\t read json file and continue conversation
` + clear_cmd +`\t\t\t clear the current conversation history, and start from scratch
` + help_cmd + `\t\t\t show this help text
` + show_cmd + `\t\t\t show current settings
` + list_models_cmd + `\t\t list available models (shows latest models first)

the current conversation will be stored in json file ` + conversation_file_name + `
--------------

`);
}

function showSettings() {
    console.log(`Current Settings:

Model name:\t\t` + model_name + `
Max token values:\t` + max_token_value +`
Temperature:\t\t` + (temperature_value == -1 ? "default" : temperature_value ) + ` 
        
`);

}

async function listModels() {

    console.log("listing models..");

    let response = await openai.listModels();

    response.data.data.sort(function(a,b) { 
        if (a.created < b.created) {
            return 1;
        }
        if (a.created > b.created) {
            return -1;
        }
        return 0;
    });

    if (response.data.data.length  == 0) {
        console.log("no models listed.\n")
        return;
    }


    for(let i=0; i < response.data.data.length; ++i) {
        let obj =response.data.data[i]; 
        let date = new Date(obj.created * 1000);
        console.log("created_at: ", date.toISOString() + " model:", obj.id, "\t\t\t\towned_by:", obj.owned_by);
    }
}


function readConversationFromFile(questionText) {
    try {
        let inFile = questionText.substring(read_file_cmd.length);
        let conversationText = fs.readFileSync( inFile );
        conversation = JSON.parse(conversationText);
        console.log(">will continue with conversation from file ", inFile);
    } catch(er) {
        console.log("error occurred: ", er);
    }
}

function writeConversationToFile(questionText) {
    try {
        let outFile = questionText.substring(read_file_cmd.length);
        fs.writeFileSync( outFile, JSON.stringify(conversation, null, 2));
        console.log(">saved conversation to file", outFile);
    } catch(er) {
        console.log("error occurred: ", er);
    }
}
 
function setTokenValue(questionText) {
    try {
        let next = questionText.substring(set_max_token_cmd.length);
        max_token_value = parseInt(next.trim());
        console.log(">setting max_token value to", max_token_value);
    } catch(er) {
        console.log("error occurred: ", er);
    }
} 

function setTemperature(questionText) {
    try {
        let next = questionText.substring(set_temperature_cmd.length);
        temperature_value = parseFloat(next.trim());
        console.log(">setting temperature value to", temperature_value);
    } catch(er) {
        console.log("error occurred: ", er);
    }

}

async function talkToRobot(questionText) {

    if (debugIt) {
        console.log("talkToRobot", questionText);
    }

    conversation.push(
        { 'role': 'user', 'content': questionText }
    );

    try {

        let args = {
            model: model_name,
            prompt: JSON.stringify(conversation),
            max_tokens: max_token_value,
        };

        if (temperature_value != -1) {
            args.temperature = temperature_value;
        }

        let completion = await openai.createCompletion(args);

        for(let i=0;i<completion.data.choices.length;++i) {
              let answer = completion.data.choices[i].text;

              if (debugIt) {
                console.log("rawAnswer: " + answer);
              }
              try {

                  let jsonAnswer = JSON.parse(answer);

                  answer = "";
                  if (Array.isArray(jsonAnswer)) {
                      for(let i=0; i<jsonAnswer.length; ++i) {

                        if (i > 0) {
                            answer += " ";
                        }
                        if (jsonAnswer[i].role != 'system') {
                            answer += jsonAnswer[i].role + ": ";
                        }
                        answer += jsonAnswer[i].content;
                      }
                  } else {
                      if (jsonAnswer.role != 'system') {
                          answer += jsonAnswer.role + ": ";
                      }
                      answer += jsonAnswer.content;
                  }

              } catch(ex) {
                  if (debugIt) {
                    console.log("not json? " + ex);
                  }
              }

              console.log("answer(" + i + "): ", answer);

              conversation.push( 
                  { 'role': 'system', 'content' : answer }
              );   
          }
    } catch(ex) {
        console.log("error: ",ex);
        conversation.pop();
    }   

    fs.writeFileSync( conversation_file_name, JSON.stringify(conversation, null, 2));
}

async function talkLoop() {

    let prefix = "{\"role\":\"system\",\"content\":";

    showHelp();

    while(true) {
        let questionText = readline.question('> ');   
        console.log(questionText);

        if (questionText.startsWith(help_cmd)) {
            showHelp();
            continue;
        }

        if (questionText.startsWith(show_cmd)) {
            showSettings();
            continue;
        }

        if (questionText.startsWith(list_models_cmd)) {
            await listModels();
            continue;
        }

        if (questionText.startsWith(clear_cmd)) {
            conversation = [];
            continue;
        }


        if (questionText.startsWith(read_file_cmd)) {
            readConversationFromFile(questionText);
            continue;
        }

        if (questionText.startsWith(save_cmd)) {
            writeConversationToFile(questionText);
            continue;
       }

        if (questionText.startsWith(set_max_token_cmd)) {
            setTokenValue(questionText);
            continue;
        }
        if (questionText.startsWith(set_temperature_cmd)) {
            setTemperature(questionText);
            continue;
        }

        await talkToRobot(questionText);
    }

}

talkLoop();


