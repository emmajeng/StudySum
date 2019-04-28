class RemoveProfileIdFromProfiles < ActiveRecord::Migration[5.2]
  def change
    remove_column :profiles, :profile_id, :integer
  end
end
