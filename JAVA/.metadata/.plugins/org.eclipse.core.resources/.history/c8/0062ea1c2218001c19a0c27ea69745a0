package com.malonwright.DojoSurvey.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class FormController {
	@RequestMapping("")
	public String index() {
		return "index.jsp";
	}
	@RequestMapping(path="/result", method=RequestMethod.POST)
	public String results(@RequestParam(value="name")String name,@RequestParam(value="dojo") String dojo,@RequestParam(value="language")String language,@RequestParam(value="comment") String comment, ModelMap modelmap){
		modelmap.put("name", name);
		modelmap.put("dojo", dojo);
		modelmap.put("language", language);
		modelmap.put("comment", comment);
		
		
		return "redirect:/results";
	}
}
