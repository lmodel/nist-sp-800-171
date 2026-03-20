package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  A catalog element with required id, title, and optional class/label
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class IdentifiedElement extends CatalogElement {

  private String title;
  private String class;
  private String label;

}