{-# LANGUAGE RankNTypes      #-}
{-# LANGUAGE TemplateHaskell #-}

module FpSolveMeFirst (fpSolveMeFirst, runTests) where
import           Test.QuickCheck.All

fpSolveMeFirst :: forall t. Num t => t -> t -> t
fpSolveMeFirst a b = c
    where c = a + b

hrFpSolveMeFirst input = output where
    sa:sb:_ = lines input
    c = fpSolveMeFirst (toInteger sa) (toInteger sb)
    output = unlines [fromInteger c]

prop_fpSolveMeFirst :: forall t. (Num t, Eq t) => t -> t -> Bool
prop_fpSolveMeFirst a b =
    a + b == fpSolveMeFirst a b

return []
runTests :: IO Bool
runTests = $quickCheckAll
