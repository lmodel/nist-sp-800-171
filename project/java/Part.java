package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  Structured narrative part containing prose and optional nested parts. Used for statements, guidance, assessment-objectives, and assessment-methods.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Part extends CatalogElement {

  private String name;
  private String class;
  private String prose;

}