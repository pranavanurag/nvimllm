===============
how could I go about making something (scrappy python script or nvim extension idk scrappy for now) like RepoPrompt but using dspy such that I can swap out dspy modules on the fly for what I need? the idea is to vibe code with pinpoint precision. ultrathink about this in the following order
1. familiarize yourself with the core ideas and some examples of DSPy
2. familirize yourself with repoprompt.com
3. think about how repoprompt, the basic idea of it, could be implemented using a python script, using dspy. do not overengineer. this is a proof of concept, keep it absolutely bare bones. we can work on this together
4. think about how we might be able to use some extensions or a keybinding based user interfacve within nvim or vscode to implement such functionality (I have no idea how we could do this as long as dspy is in python. maybe I can host a service on some port have nvim / vscode call that port on my local machine)
=============



=============
this is way too complicated to be bare bones. implement hello world for nvim. the flow should be

<leader> l (I dont know much about nvim leader key stuff, but I want to say hey nvim, take this selected text and send it to an llm. then , append from the end of the selected text the response from the llm service)

takes the current line in the current buffer, sends it to dspy llm gpt4o with answer this programming question as the dspy signature requirement
call the llm and then return the response back. in fact, fuck dspy. just call the openai API in the dspy scaffold for now
=============
