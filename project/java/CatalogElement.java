package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  Base class for catalog elements with id, props, links, and parts
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class CatalogElement  {

  private String id;
  private List<Property> props;
  private List<Link> links;
  private List<Part> parts;

}