<%inherit file="default.mako" />
<%block name="title">Prihlasenie</%block>
<%block name="page_content">
% for task in tasks:
    <div> ${task[0].task} assigned to ${task[2]}
% endfor
</%block>
