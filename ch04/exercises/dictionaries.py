article="NEW YORK (AP) — With less than two months until the midterm elections, progressive Democrats are facing a test of their power. \n Their party is heading into the final stretch of the campaign with a robust set of legislative accomplishments that include long-term progressive priorities on issues ranging from prescription drug prices to climate change. But the left has also faced a series of disappointments as Democratic voters from Ohio to Illinois to Texas rejected high-profile progressive challengers to moderates or incumbent members of Congress during the primary season. \n The  frustration is particularly acute in New York, where Rep. Alexandria Ocasio-Cortez defeated one of the highest-ranking congressional Democrats four years ago, injecting fresh energy among the party's most liberal voters. This year, however, New York City Democrats chose Dan Goldman, a former federal prosecutor who is more of a centrist, over several progressive rivals, including freshman Rep. Mondaire Jones. About 30 miles north in the Hudson River Valley, a powerful establishment candidate, Rep. Sean Patrick Maloney, defeated a state lawmaker running to his left and backed by Ocasio-Cortez. \n Those setbacks have raised fresh questions about the progressive movement's standing among Democrats. Progressive leaders urge against reading too much into those losses, particularly in New York, where repeated elections this summer after a redistricting battle left some voters disoriented or disengaged."

dictionary={
  "congressional":"spaaaaace",
  "Republican":"piano accordionist",
  "Democrat":"chromatic button accordionist",
  "senator": "magical wizard",
  "Rep.": "unmagical wizard",
  "leaders":"goblins",
  "Congress": "the mushroom house",
  "progressive": "short",
  "party": "book club"
}

for key, value in dictionary.items():
  article=article.replace(key,value)

print(article)