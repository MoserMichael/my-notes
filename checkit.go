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

func main() {

	mapArg := map[string]string{
		"first_key": "first_val",
	}

	passStringMap(mapArg)

	if mapArg["first_key"] != "first_key" {
		fmt.Print("maps are passed by reference\n")
	} else {
		panic("You thought maps are passed by value? wrong!")
	}

	vecStr := []string{"first", "second", "third"}

	passStringVec(vecStr)

	if vecStr[0] != "first" {
		fmt.Printf("arrays are passe by reference\n")
	} else {
		panic("You thought arrays are passed by value? wrong!")
	}

	structStr := StrStruct{firstVal: "first"}

	passStringStruct(structStr)

	if structStr.firstVal == "first" {
		fmt.Printf("Structs are passed by value\n")
	} else {
		panic("You thought structs are passed by reference? Wrong, this is not java!")
	}

	fmt.Printf(`********************************
now you learned something
(yeah, and simple go is confusing the heck out of me)
(why are there always such inconsistencies???)
********************************`)

}
