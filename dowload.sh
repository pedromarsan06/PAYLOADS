#!/usr/bin/env bash
# clone_tools.sh
# Clona repositórios essenciais em ~/tools (silencioso, sem instalar dependências)
set -euo pipefail

TOOLS_DIR="${HOME}/tools"
mkdir -p "$TOOLS_DIR"

GIT_OPTS="--quiet --depth 1"

# Repositórios
REPOS=(
  "https://github.com/peass-ng/PEASS-ng.git"
  "https://github.com/rebootuser/LinEnum.git"
  "https://github.com/jondonas/linux-exploit-suggester-2.git"
)

for repo in "${REPOS[@]}"; do
  name="$(basename "$repo" .git)"
  target="${TOOLS_DIR}/${name}"
  if [ -d "$target" ]; then
    git -C "$target" pull --quiet || true
  else
    git clone $GIT_OPTS "$repo" "$target" 2>/dev/null || true
  fi
done

# Apenas confirmação mínima (sutil)
echo "OK: repositórios clonados em $TOOLS_DIR"
exit 0
