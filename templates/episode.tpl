<h1>{{nameOfSkill}}</h1>

<br>
<ul class="skillers-results">
% for people in result:
<li class="people-results" onclick="location.href='/profile/{{people[0]}}';">{{people[1]}}</li>
% end
% if not result:
    No Results :(
% end

</ul>