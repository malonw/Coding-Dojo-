<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>  
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Login</title>
</head>
<body>
	<div class="container">
	<h1>Welcome to Albums dot com</h1>
	<h2>Register Here</h2>
		<form:form action="/registerUser" method ="post" modelAttribute="user">
			<div class = "form-group row">
				    <p>
				        <form:label path="firstName">First Name</form:label>
				        <form:errors path="firstName"/>
				        <form:input path="firstName" class="form-control"/>
				    </p>
				 </div>
				 <div class = "form-group row">
				    <p>
				        <form:label path="lastName">Last Name</form:label>
				        <form:errors path="lastName"/>
				        <form:input path="lastName"  class="form-control"/>
				    </p>
				 </div>
			     <div class = "form-group row">
				   <p>
				        <form:label path="email">Email</form:label>
				        <form:errors path="email"/>
				        <form:input path="email"  class="form-control"/>
				    </p>
				 </div>
			     <div class = "form-group row">
				    <p>
				        <form:label path="password">Password:</form:label>
				        <form:errors path="password"/>
				        <form:input path="password" type="password" class="form-control"/>
				    </p>
				  </div>
			    	<div class = "form-group row">
				    <p>
				        <form:label path="confirmpassword">Password:</form:label>
				        <form:errors path="confirmpassword"/>
				        <form:input path="confirmpassword" type="password" class="form-control"/>
				    </p>
				 </div>
			    <input class="btn-primary" type="submit" value="Submit"/>

		</form:form>
	</div>
	<h3>Login</h3>
	<div class="col">
	<form action="/login" method ="post">
	<label> Email Address</label>
	<input type="email" name="email"/>
	<label>Password</label>
	<input type="password" name="password"/>
	<button class="btn-primary" type="submit">Submit</button>
	</form>
	</div>
</body>
</html>