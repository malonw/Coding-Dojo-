package com.student.malonwright.routing.controllers;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("dojo/{string}")
@ResponseBody
public class DojoController {
	@RequestMapping("/dojo")
	public String dojo( ) {
		return "The dojo is awesome!";
	}
@ResponseBody
	public String burbank(@PathVariable String string) {
		return "Burbank Dojo is located in Southern California";
	}
@ResponseBody
	public String sanjose(@PathVariable String string) {
		return "SJ dojo is the headquarters";
	}
}
