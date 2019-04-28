class AddProfileIdToProfile < ActiveRecord::Migration[5.2]
  def change
    add_column :profiles, :profile_id, :integer
  end
end
