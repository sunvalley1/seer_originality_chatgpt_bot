set -eu
pin=3e3ec397a8a03998026cf9e8afaedf049102283a
test "$(git ls-tree HEAD | awk -F '\t' '$2 != "run"' | git mktree)" = "$pin"
git diff --quiet
git diff --cached --quiet
test -z "$(git ls-files --others --exclude-standard)"
test -z "$(git ls-files --others --ignored --exclude-standard -- run ':(exclude,glob)run/.lock.deep-r3-trade/**' ':(exclude,glob)run/*/exec-tmp/**' ':(exclude,glob)run/*/f-tmp/**' ':(exclude,glob)run/*/g-tmp/**' ':(exclude,glob)run/*/halfb-tmp/**' ':(exclude,glob)run/*/recovery-tmp/**')"
test "$(git remote get-url origin)" = https://github.com/sunvalley1/seer_originality_chatgpt_bot.git
test "$(git remote get-url --push origin)" = https://github.com/sunvalley1/seer_originality_chatgpt_bot.git
git -c core.hooksPath=/dev/null fetch --no-tags origin main
test "$(git ls-tree origin/main | awk -F '\t' '$2 != "run"' | git mktree)" = "$pin"
git merge-base --is-ancestor HEAD origin/main
git -c core.hooksPath=/dev/null merge --ff-only origin/main
test "$(git ls-tree HEAD | awk -F '\t' '$2 != "run"' | git mktree)" = "$pin"
git diff --quiet
git diff --cached --quiet
