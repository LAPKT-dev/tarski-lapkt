# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Changed
### Added
### Removed
### Deprecated
### Fixed


## [0.7.1] 2022-03-??
### Changed
 - Added support for `clingo`'s `Pypi` distribution. This means it is no longer necessary to install manually
    `cligo`/`gringo`. Some `tarski` internal interfaces were changed, please review these changes if you have
    codes coupled to the ASP-based grounding components (#123).
 - `gringo` now is an `extra` requirement of the package `tarski`. In order to install `tarski` with the `clingo`
    support, issue the command `$ pip install tarski[gringo]`. 
 - ASP-based grounding components will try to fall back to "manually installed" `clingo`/`gringo` distributions,
    using the same heuristic procedure we were using in `0.7.0`
### Added
 - Temporal planning model:
   - Added concept of post-condition (i.e. `at end` conditions) `Action` class
   - Added concept of duration to `Action` class
   - Added concept of grounding constraints to `Action` class
 - Naive grounding features:
   - Added method to exhaustively ground terms with subterms that are constants. For instance, the term `foo(x, a)`
   where `x` is a variable and `a` is a constant can be now grounded taking into account that the second argument of
   `foo` is already fixed to `a`.
 - Error reporting and handling:
   - `UndefinedTerm`: added name of term as an argument. This enables processing exception data, for instance,
   to initialise such terms to some value like `infty` or force the failure to ground some structural element in
   a domain, such as an action.
 - PDDL parsing (WIP):
   - Current implementation using `ply` package, version 3.11. Eventually will be refactored for `sly`. Plan is 
   eventually to parse correctly and generate instance structural elements for PDDL 3.1.
   - Supported features:
     - Instantaneous actions
     - Durative actions
       - Care has been taken so the parser allows the keyword `at` to be used as a predicate/function/type identifier
     - Derived predicates
     - Object fluents
     - Metrics associated with IPC formulations of temporal planning
   - Partial support:
     - Conditional effects
     - Quantified conditions in preconditions, conditional effects and derived predicates
     - Arithmetic expressions and effects
 - New formula visitor: `CollectEqualityAtoms`
   - What it says on the tin: collects equality atoms that appear as subformulas of a given formula
 - New `pip` dependency: `ply`
### Removed
### Deprecated
 - Disabled references to Functional STRIPS `counters` instances in tests
### Fixed
 - Fixed issue with parsing Fast Downward's SAS instance data, due to whitespace not being ignored as it should (#121)
 - Fixed issue with printing of types in untyped domains (#113)
 - Use real instead of integer numbers by default when parsing with strict_with_requirements=False (#114)
 - `FirstOrderLanguage.is_subtype`: it is now checked if there is a path connecting two types in the type hierarchy. If
    that is the case, this fact is recorded in the dictionary `indirect_ancestor_sorts`. Whenever a change is made 
    in the type hierarchy (e.g. adding a new sort or changing the parent of a sort), the cache is invalidated.
 - Fixed issue with equality predicates trying to coerce the right hand side to a constant when the left hand side is
    a term
 
    
## [0.7.0]
### Added
  - Added some basic forward search capabilities (#101).
  - Import psutil module conditionally, to offer better support for non-Linux 
    platforms where it is not available (see discussion in #99). 

### Removed
  - Removed support for `PySDD` and `sdd` extra, which was largely unused, and
    hard to integrate into the CI testing.

### Deprecated
  - Model.set() is now deprecated

### Fixed
 - Fixed a bug in `check_hypergraph_acyclicity` reported by @abcorrea.


## [0.6.0]- 2020-09-18
### Changed
  - Switched license to the Apache Software Licence 2.0 (#92)

### Fixed
  - Minor bugfixes and improvements.
  - Better compliance with pylint warnings and errors.  


## [0.5.1] - 2020-04-17
### Fixed
  - Fixed some silly releasing mistakes... through a new release :-)


## [0.5.0] - 2020-04-17
### Added
  - Improved documentation (still work in progress though).
  - Added methods to simplify problems, actions, logical expressions based on evaluation
  of static atoms and terms.
  - Added method to compile away negated literals in action preconditions, action effect conditions
  and goal, using the standard mechanism of creating additional predicates.
  - Almost all benchmarks from the IPC competitions 2008, 2011, 2014, 2018 are now correctly parsed by Tarski.
  The unit tests also make sure this keeps being true. The only domain that Tarski cannot parse
  correctly is Tidybot, where "cart" is used both as type name and object name. This does not bode well with 
  the assumptions made in Tarski first-order languages. Problems from domains Floortile and GED need to be parsed
  with caution as well, by using, respectively, the parser options `strict_with_requirements=False` and
  `case_insensitive=True`, since the first one uses action costs without declaring them in the "requirements" section,
  whereas the second one uses lowercase in the domain file, and uppercase in the instance file.
  - Improved support for representation and parsing of action costs. 
  - Added methods to check applicability of an action in a state (model) and to progress a state through an action. 
  - Added some methods to the `fstrips.representation` module to check and compute delete-free relaxations of problems.
  - Modularize Tarski dependencies so that the use and  installation of numpy, scipy, etc. is optional.
  - Generation of action schema CSPs.


## [0.4.0] - 2019-12-28
### Changed
- Almost-identical methods `approximate_symbol_fluency` and `classify_symbols` have been merged into one
  single method `approximate_symbol_fluency`.

### Added
 - Preliminary [readthedocs documentation](https://tarski.readthedocs.io) integrated in the repository.
   CI tests the documentation build as well.
 - Integration with the [PySDD package](https://github.com/wannesm/PySDD) for sentential decision diagrams
 to process action schema preconditions.
 - Implementation of a `project_away_effect_free_variables_from_problem` transformation that for each action schema
   compiles into existential variables all action parameters that are not used in the action effects
    ([#63](https://github.com/aig-upf/tarski/issues/63)).
 - Implementation of a `compile_universal_effects_away` transformation that expands universal effects in actions. 
 - Reachability module now processes problems with cost-related functions (010d79df)
 - Preliminary implementation of a library of benchmark generators
    ([#43](https://github.com/aig-upf/tarski/issues/43)).
 - Added some preliminary support for the NDL representation language.

### Fixed
 - Fixed some minor bugs in FSTRIPS writer.
 - Fixed bug in ReachabilityLPCompiler when problem has an action and a predicate with the same name (7e9a684).
 - Remove temporary files created by the LP based grounder.
 - Model.list_all_extensions now returns empty extensions if necessary (ffbc96d1)


## [0.3.0] - 2019-08-03

### Added
 - Preliminary implementation of a `tarski.fstrips.representation` module with some representational queries 
   and transformations. 
 - Preliminary integration with [mypy static typing analysis](https://github.com/python/mypy) which is
   checked now in the CI tests.
 - Add helper function `find_domain_filename` to infer domain filenames from instance filenames.
 - Add `collect_unique_nodes` method to collect all AST nodes of any FSTRIPS expression.
 - Add namespace accessor `lang.ns` to FOL objects to allow direct access to any language element.
 
### Fixed
 - Fixed bug with fluent / static symbol classification [#66](https://github.com/aig-upf/tarski/issues/66).
 - Fixed bug with multiple conditional effects in [FSTRIPS / PDDL parser](https://github.com/aig-upf/tarski/commit/c89ac31623171b78689d5d0ae3eca07c2be2ad71).
 - Fix bug in printing of FSTRIPS instances [#69](https://github.com/aig-upf/tarski/issues/69).
 - Some other minor bugfixes.


## [0.2.0] - 2019-07-16
### Added
 - Parsing and writing of Functional STRIPS and PDDL encodings of classical planning problems.
 - Parsing and writing of RDDL encodings of Markov Decision Processes (MDPs) and hybrid planning problems.
 - Answer Set Programming-based grounding and reachability analysis for classical planning problems.
 - Description Logics module for classical planning problems.
 - Support for Existentially and Universally Quantified effects in Functional STRIPS and PDDL domain descriptions.
 - Syntax for elementary linear algebra operations with vectors and matrices.
 - Support for the evaluation of expressions involving matrices, vectors and scalars.
 - Expression simplification.


## [0.1.0] - 2018-09-15

First public release.
