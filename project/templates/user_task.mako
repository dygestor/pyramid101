<%inherit file="default.mako" />
<%block name="page_content">
<div>
	Showing tasks for user ${user}
</div>
% for task in tasks:
    <div> ${task[0].task} assigned to ${user}
% endfor
</%block>
