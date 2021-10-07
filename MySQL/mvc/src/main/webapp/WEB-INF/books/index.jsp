<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>  
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Books</title>
</head>
<body>
<div class ="all">
	<h1>All Books</h1>
		<table>
			<thead>
				<tr>
					<th>Title</th>
					<th>Description</th>
					<th>Language</th>
					<th>Number Of Pages</th>
				</tr>
			</thead>
			<tbody>
			
				<c:forEach items="${books }" var = "book">
				<tr>
					<td><a href="/books/show/${book.id }"><c:out value="${book.title }"/></a></td>
					<td><c:out value="${book.description }"/></td>
					<td><c:out value="${book.language }"/></td>
					<td><c:out value="${book.numberOfPages }"/></td>
				</tr>
				</c:forEach>
			</tbody>
		</table>
	</div>
		<p>
		<a href="/books/new">New Book</a>
		</p>
</body>
</html>