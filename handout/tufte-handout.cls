% -------------------------------------------------------------------------- %
% NOTICE
% This file has been modified from the original tufte-handout.cls available at
% https://github.com/Tufte-LaTeX/tufte-latex
%
% Changes made (all concerning comments, no executable modifications):
% 	Define sections with 79-char wide lines instead of %%
%   Remove redundant comments
%   Correct typo in TODO
%   Harmonize line spacing between sections
% -------------------------------------------------------------------------- %


% -------------------------------------------------------------------------- %
% Require necessary LaTeX2e version and provide the class
\NeedsTeXFormat{LaTeX2e}[1994/06/01]
\ProvidesClass{tufte-handout}[2010/03/28 v3.5.1 Tufte-handout class]


% -------------------------------------------------------------------------- %
% Declare we're tufte-handout
\newcommand{\@tufte@class}{article}% the base LaTeX class (defaults to the article/handout style)
\newcommand{\@tufte@pkgname}{tufte-handout}% the name of the package (defaults to tufte-handout)


% -------------------------------------------------------------------------- %
% Load common style elements
\input{tufte-common.def}


% -------------------------------------------------------------------------- %
% TODO The abstract should be printed on its own page if the `titlepage'
% option was specified.
\renewenvironment{abstract}
  {\begin{quotation}\if@tufte@sfsidenotes\begin{sffamily}\fi}
  {\if@tufte@sfsidenotes\end{sffamily}\fi\end{quotation}}


% -------------------------------------------------------------------------- %
% All other customizations / packages beyond the default style elements are
% located in a separate file, "tufte-handout-local.tex" in this directory.
\IfFileExists{tufte-handout-local.tex}{%
  \input{tufte-handout-local}%
  \@tufte@info@noline{Loading tufte-handout-local.tex}%
}{}


% -------------------------------------------------------------------------- %
% End of file
\endinput
