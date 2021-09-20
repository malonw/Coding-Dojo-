package com.student.malonwright.routing.controllers;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/dojo")

public class DojoController {
	@RequestMapping("/{string}")
	public String dojo( @PathVariable("string") String string) {
		if (string.equals("dojo")) {
			return "The dojo is awesome!";
		}else if (string.equals("burbank")) {
			return "Burbank Dojo is located in Southern California";
	}else if(string.equals("sanjose")){
			return "SJ dojo is the headquarters";
	}else {
		return "Location not found";
	
	}
}
}
