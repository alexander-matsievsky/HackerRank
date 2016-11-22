{-# LANGUAGE LambdaCase      #-}
{-# LANGUAGE TemplateHaskell #-}
module PrefixCompression(runTests) where
import           Test.QuickCheck
import           Text.Printf

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    output = unlines . map print' $ [p, a', b']
    print' :: String -> String
    print' string = printf "%d %s" (length string) string
    a:b:_ = lines input
    p = map fst . takeWhile (uncurry (==)) $ zip a b
    a' = drop (length p) a
    b' = drop (length p) b

prop_run = run "\
\abcdefpr\n\
\abcpqr" == "\
\3 abc\n\
\5 defpr\n\
\3 pqr\n"

prop_run1 = run "\
\kitkat\n\
\kit" == "\
\3 kit\n\
\3 kat\n\
\0 \n"

prop_run2 = run "\
\puppy\n\
\puppy" == "\
\5 puppy\n\
\0 \n\
\0 \n"

return []
runTests = $quickCheckAll
