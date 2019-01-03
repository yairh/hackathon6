<h1>{{nameOfCat}}</h1>

<br>
<ul class="skills-results">
% for skill in result:
<li class="skill-result" onclick="Browse.loadEpisode('{{skill[1]}}', '{{skill[0]}}')">{{skill[2]}}</li>
% end
% if not result:
    No Results :(
% end

</ul>