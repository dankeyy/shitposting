-- The boring details --
{-# LANGUAGE OverloadedRecordDot, DuplicateRecordFields, DatatypeContexts  #-}

import Text.Printf
import Prelude hiding ((+))
(+)=(++)

data Person = Person { name :: String,  getName :: () -> String};
data Company = Company { name :: String, owner :: Person, getName :: () -> String, getOwner :: () -> Person};
data Show poop => Out poop = Out { println :: poop -> IO () }
data System poop = System  { out :: Out poop };
system = System  { out = Out { println = print } };

-- The beauty --
main = do
  let dictator = Person {
            name = "dankey",
            getName = (\_ -> dictator.name)
  };

  let company = Company {
        owner = dictator,
        name  = "Dumbass Corp.",
        getName = (\_ -> company.name),
        getOwner = (\_ -> company.owner)
  };

  system.out.println(company.getName() + " is run by " + (company.getOwner()).getName());
  --"Dumbass Corp. is run by dankey"
