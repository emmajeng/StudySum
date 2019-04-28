class AddUserIdToDocument < ActiveRecord::Migration[5.2]
  def change
    add_reference :documents, :users, foreign_key: true
  end
end
