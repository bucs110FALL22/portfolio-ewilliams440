import pygame
pygame.init()

linecolor=("black")
windowcolor=("white")
fontcolor=("black")
upper_limit=20
iters={}
max_so_far=1
max_val=2
scale=5
fontsize=40
fontposition=(10,10)

display=pygame.display.set_mode()
font=pygame.font.Font(None,fontsize)

for start in range(2,upper_limit):
  n=start
  count=0
  display.fill(windowcolor)
  while n!=1:
    count=count+1
    if n%2 ==0:
      n=n/2
    else:
      n=n*3+1
  iters[start*scale]=count*scale
  if max_so_far<count:
    max_so_far=count
    max_val=start
  if start>2:
    for i in range(start-2):
      coord1=list(iters.items())[i]
      coord2=list(iters.items())[i+1]
      pygame.draw.lines(display,linecolor,False,[coord1,coord2])
  pygame.time.wait(1000)
  msg=font.render("Max: "+str(max_so_far),False,fontcolor)
  new_display=pygame.transform.flip(display, False, True)
  display.blit(new_display,(0,0))
  display.blit(msg,fontposition)
  pygame.display.flip()