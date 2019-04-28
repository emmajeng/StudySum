class RemoveUserFromDocuments < ActiveRecord::Migration[5.2]
  def change
    remove_reference :documents, :users, foreign_key: true
  end
end
