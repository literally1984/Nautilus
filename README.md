# Nautilus
Serverless console based chat program made with PyDrive2.
# How To Use:
After installing the program files from GitHub, they can be put anywhere. Just make sure to keep all files in one place.
 
To start using Nautilus, run 'setup.py' and follow the instructions it provides. While you can run it with an IDE or something similar, I encourage you to run it with [Windows Terminal](https://github.com/microsoft/terminal#installing-and-running-windows-terminal)* (Windows) or [iTerm2](https://iterm2.com/)** (Mac). See [this link](https://www.wikihow.com/Open-a-Python-File#Using-Python-at-the-Command-Line) for help on running a Python file in Windows Terminal or iTerm2.

*Previously, it was encouraged to run Nautilus with the regular Windows Command Prompt. However, with the addition of emoji support in release 2.1.0, Command Prompt is now useless because it cannot display Unicode, or at least emojis.

**Previously, it was encouraged to run Nautilus with the regular Mac Terminal. However, with the addition of the 'images' feature, Terminal simply does not work because the 'images' feature needs truecolor support.

# Emojis
See [this file](https://github.com/literally1984/Nautilus/blob/main/emojis.md) for a complete list of all emojis supported by Nautilus.
 
# Markup
Wanna spice up your messages with colors? Or make your words have a bigger impact by bolding them? Lucky for you, Nautilus supports just that!
To use colors in your messages you can do something like:

```<red>Hello there!</red>```

Nautilus supports black, red, green, yellow, blue, magenta, cyan, and white colors! It also supports their lighter counterparts. For example:

```<light-black>This should be hard to read!</light-black>```

Also, if you want to have your text set against a background, your message may look a little like:

```<BLACK>This should be really hard to read!</BLACK>```

And again, to use their light variants:

```<LIGHT-CYAN>Wow, light cyan is a thing??</LIGHT-CYAN>```

You can also use rgb, hex, and xterm colors. fg is 'foreground' which just means your text will be colored by the color picked and bg is 'background', which I already talked about above. Example:

```<fg 10>This text is a green color. Pretty cool, right?</fg 10>```

It wouldn't be markup without markup styles! The following would be bolded and underlined:

```I <bold><underline>love</underline></bold> Nautilus!```

For full coverage on everything that you can do with Nautilus's markup, check out the [library](https://github.com/gvalkov/python-ansimarkup) that Nautilus uses.

# Images
Images can be uploaded to Nautilus. They'll be pixelated, however. To use this feature, have your message set up like this:

``` `path to image file|caption you might want to add(optional)` ```

An example:

``` `C:\Users\Nautilus\Downloads\unnamed.jpg` ```

The output would be:

<img width="309" alt="untitled-Nautilus" src="https://user-images.githubusercontent.com/85363779/128793102-e08ac61d-013c-4b9d-8af7-d1008f501bdd.PNG">
 
 The original image was:
 
![unnamed](https://user-images.githubusercontent.com/85363779/128643929-34220cc0-c1f2-4742-8196-97837f76323d.jpg)

# Replies
Replies are in their early stage of development. They aren't perfect, since you'll have to type out the message you're replying to manually, but they aren't that bad either.
To form a reply, make your message look like the following:

```,Message you're replying to.|Your reply.,```

If you were to type out the message above, it would render as:

<img width="400" alt="reply" src="https://user-images.githubusercontent.com/85363779/128943235-1445b2d2-6ba8-495b-8618-c192974c2de6.png">
