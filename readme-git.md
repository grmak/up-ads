## GIT BÁSICO

# 0. Clonar o repositório
git clone https://github.com/grmak/up-ads.git

# 1. Verificar status (já feito)
git status

# 2. Commit
git commit -m "feat: renomeia arquivos aula03 e adiciona novos exercícios"

# 3. Verificar se commit foi criado
git log --oneline -1

# 4. Enviar para o GitHub/GitLab
git push origin main

# 5. Confirmar envio
git status
# Deve mostrar: "nothing to commit, working tree clean"
