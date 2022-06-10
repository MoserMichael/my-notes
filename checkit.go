package main

import "fmt"

type StrMap map[string]string

func passStringMap(m StrMap) {
	m["first_key"] = "changed_val"
}

type StrVec []string

func passStringVec(m StrVec) {
	m[0] = "changed_val"
}

type StrStruct struct {
	firstVal string
}

func passStringStruct(m StrStruct) {
	m.firstVal = "changed_val"
}

/*
The actual output:

function parameters that are maps are passed by reference
function parameters that are arrays are passed by reference
function parameters that are structs are passed by value !!!

map lookup of sequence, the value is returned by reference!
you got a string from map to scalar lookup
map lookup of scalar, the value is returned by value
map lookup of struct, the value is returned by value

********************************
now you learned something
(yeah, and simple go is confusing the heck out of me)
(why are there always such inconsistencies???)
********************************
*/
func main() {

	mapArg := map[string]string{
		"first_key": "first_val",
	}

	passStringMap(mapArg)

	if mapArg["first_key"] != "first_key" {
		fmt.Print("function parameters that are maps are passed by reference\n")
	} else {
		panic("You thought maps are passed by value? wrong!")
	}

	vecStr := []string{"first", "second", "third"}

	passStringVec(vecStr)

	if vecStr[0] != "first" {
		fmt.Printf("function parameters that are arrays are passed by reference\n")
	} else {
		panic("You thought arrays are passed by value? wrong!")
	}

	structStr := StrStruct{firstVal: "first"}

	passStringStruct(structStr)

	if structStr.firstVal == "first" {
		fmt.Printf("function parameters that are structs are passed by value !!!\n\n")
	} else {
		panic("You thought structs are passed by reference? Wrong, this is not java!")
	}

	mapToVector := map[string]StrVec{
		"first": []string{"one", "two", "three"},
	}

	val, _ := mapToVector["first"]

	val[0] = "changed_it"

	if mapToVector["first"][0] != "one" {
		fmt.Printf("map lookup of sequence, the value is returned by reference!\n")
	} else {
		panic("You were wrong, the lookup returned a reference value!\n")
	}

	mapToString := map[string]string{"one": "first"}
	strVal, _ := mapToString["one"]
	fmt.Printf("you got a %T from map to scalar lookup\n", strVal)
	strVal = "actually-this-value-is-not-used"

	if mapToString["one"] == "first" {
		fmt.Printf("map lookup of scalar, the value is returned by value\n")
	} else {
		panic("You were wrong. map lookup with scalar values does not return a reference\n")
	}

	mapStrToStruct := map[string]StrStruct{
		"one": StrStruct{firstVal: "first"},
	}

	stuctVal, _ := mapStrToStruct["one"]
	stuctVal.firstVal = "changed_it?"

	if mapStrToStruct["one"].firstVal == "first" {
		fmt.Printf("map lookup of struct, the value is returned by value\n")
	} else {
		panic("You were wrong. map lookup of struct value does not return a reference value\n")
	}

	fmt.Printf(`
********************************
now you learned something
(yeah, and simple go is confusing the heck out of me)
(why are there always such inconsistencies???)
********************************`)

}
