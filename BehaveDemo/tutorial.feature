Feature: showing off behave

Scenario: run a simple test
	Given we have behave installed
	When we implement a test
	Then behave will test it for us!
	Then I call some other steps

@wip
Scenario: some scenario
  Given a set of specific users
     | name      | department  |
     | Barry     | Beer Cans   |
     | Pudey     | Silly Walks |
     | Two-Lumps | Silly Walks |

  When login with




Scenario Outline: Blenders
   Given I put <thing> in a blender,
    then it should transform into <other thing>

 Examples: Amphibians
   | thing         | other thing |
   | Red Tree Frog | toxic waste |

 Examples: Consumer Electronics
   | thing         | other thing |
   | iPhone        | toxic waste |
   | Galaxy Nexus  | toxic waste |  