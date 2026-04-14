Review Structure (WITH EXAMPLES):

1. **Suggested Commit Message**  
   *Example:*  
   `fix: correct null pointer handling in comment service`

2. **Readability & Flow (Not OK)**  
   *Example:*  
   - Deep nested logic in `UpdateCommentHandler()` makes control flow unclear.  
   - Suggested refactor:  
     ```go
     if err := validate(input); err != nil {
         return err
     }
     return svc.UpdateComment(ctx, input)
     ```

3. **Naming & Documentation (Not OK)**  
   *Example:*  
   - Variable `pcd` is ambiguous. Rename to `parentCommentID`.  
   - Function `processData()` is too generic—rename to `buildCommentUpdatePayload()`.
   - FilePath: post/increase_user_reaction.go
      Fix: Update gorm.Expr("post_users.total + 1") to gorm.Expr("user_reactions.total + 1").

4. **Complexity & Logic (OK)**  
   *Example:*  
   Good - No issues found

5. **Bugs, Security & Edge Cases (Not OK)**  
   *Example:*  
   - Missing nil check before accessing `comment.Parent`.  
   - Add validation:  
     ```go
     if comment == nil {
         return errors.New("comment not found")
     }
     ```

6. **Best Practices & Performance (Not OK)**  
   *Example:*  
   - Duplicate DB queries inside a loop; move query outside or batch:  
     ```go
     comments, err := repo.GetCommentsByIDs(ids)
     ```

7. **Merge Decision (Not OK)**  
   *Example:*  
   **No — must fix issues in sections: Readability, Naming, Bugs, Performance**
