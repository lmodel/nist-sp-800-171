package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  Root wrapper for SP 800-171 catalog content
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SP800171Document  {

  private CatalogBody catalog;

}