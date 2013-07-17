<%inherit file="default.mako" />
<%block name="page_content">
<div>
	<form name="UserForm" id="UserForm" method="POST">
	    Name: <input type="text" name="name" id="name" /><br />
    	Email: <input type="text" name="email" id="email" /><br />
    	Task: <input type="text" name="task" id="task" /><br />
    	<input type="submit" value="Odoslať" />
    </form>
</div>
</%block>
