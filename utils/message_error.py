class ErrorMessage:    
    
    # DELETE
    def delete_success(self, objecto: str) -> str:
        return f'{objecto} eliminado com sucesso'
    
    def delete_sucess_log(self, objecto: str, id: int) -> str:
        return f'{objecto} com o código {id} eliminado com sucesso'
    
    def delete_error(self, objecto: str) -> str:
        return f'Erro ao eliminar o {objecto}. Por favor, notificar a equipa técnica'
    
    def delete_error_log(self, objecto: str, id: int, msn) -> str:
        return f'Erro ao eliminar o {objecto} com o código {id}. Message: {msn}'
    
    
    # ERROR
    def error_size(self, objecto: str) -> str:
        return f'Erro {objecto} não válido.'
    def error_status(self, objecto: str) -> str:
        return f'Erro! Estado do(a) {objecto} deve ser diferente de criado.'
    def error_payment(self, objecto: str) -> str:
        return f'Erro! valor do {objecto} inválido.'
    def date_formate(self, objecto: str) -> str:
        return f'Erro formato da {objecto} não válido.'
    def date_error(self, date_start: str, date_end: str) -> str:
        return f'Erro a data inicial {date_start} não pode ser maior que a data final {date_end}.'
    def activity_error(self, objecto: str) -> str:
        return f'Erro! Não é possível eliminar porque a actividade {objecto} já tem elementos inscritos.'
    def activity_error_log(self, objecto: str, qtd: int) -> str:
        return f'Erro! Não é possível eliminar porque a actividade {objecto} já tem {qtd} elementos inscritos.'
    
    # EXISTS 
    def exists(self, objecto: str) -> str:
        return f'{objecto} já se encontra registado (a).'
    
    def exists_log(self, objecto: str) -> str:
        return f'{objecto} já se encontra registado (a).'
    
    
    # INSERT
    def insert_success(self, objecto: str) -> str:
        return f'{objecto} salvo com sucesso.'
    
    def insert_success_log(self, objecto: str) -> str:
        return f'{objecto} salvo com sucesso.'
    
    def insert_error(self, objecto: str) -> str:
        return f'Erro ao salvar o {objecto}. Por favor, contactar a equipa técnica'
    
    def insert_error_log(self, objecto: str, msn) -> str:
        return f'Erro ao salvar o {objecto}. Message: {msn}'
    
    
    # LIST
    def list_success(self, objecto: str) -> str:
        return f'{objecto} carregados com sucesso.'
    
    def list_success_log(self, objecto: str, qtd_itens: int) -> str:
        return f'{objecto} carregados com sucesso. Total Itens: {qtd_itens}'
    
    def list_error_log(self, objecto: str, msn) -> str:
        return f'Erro ao carregar o {objecto}. Mensagem: {msn}'
    
    def list_error(self, objecto: str) -> str:
        return f'Erro ao carregar o {objecto}. Por favor, contactar a equipa técnica'
    
    
    # NOT FOUND
    def not_found(self, objecto: str) -> str:
        return f'Erro! {objecto} não encontrado. Por favor, notificar a equipa técnica'
    
    def not_found_log(self, objecto: str, id: int) -> str:
        return f'Erro! {objecto} com o código {id} não encontrado.'
    
    
    # UPDATE
    def update_success(self, objecto: str) -> str:
        return f'Dados do {objecto} actualizados com sucesso.'
    
    def update_success_log(self, objecto: str) -> str:
        return f'Dados do {objecto} actualizados com sucesso.'
    
    def update_error(self, objecto: str) -> str:
        return f'Erro ao actualizar os dados do {objecto}. Por favor, contactar a equipa técnica'
    
    def update_error_log(self, objecto: str, msn) -> str:
        return f'Erro ao actualizar os dados do {objecto}. Message: {msn}'
    
    


