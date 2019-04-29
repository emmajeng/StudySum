class DocumentsController < ApplicationController
   def index
      # @documents = Document.all
      #where('"profile_id" LIKE :id', :id => current_user.id)
      # temp_user = current_user.id
      # @documents.user_id = temp_user.documents.all
      @documents = Document.where(:user_id => current_user.id)

      
   end
   
   def new
      @document = Document.new
   end
   
   def create
      @document = Document.new(document_params)
      @document.user_id = current_user.id
      
      if @document.save
         redirect_to documents_path, notice: "The document #{@document.name} has been uploaded."
      else
         render "new"
      end
      
   end
   
   def destroy
      @document = Document.find(params[:id])
      @document.destroy
      redirect_to documents_path, notice:  "The document #{@document.name} has been deleted."
   end
   
   private
       def set_document
         @document = Document.find(params[:id])
       end
   
      def document_params
         params.require(:document).permit(:name, :attachment, :user_id)
      end
end