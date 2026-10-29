package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.0 */
import java.util.List;
import lombok.*;

/**
  A publication that SP 800-171 lists under a requirement's references, by the short name the publication gives it, with the full citation and the address NIST's catalog gives it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Sp800171Reference  {

  private String citedPublication;
  private String citedPublicationCitation;
  private String citedPublicationUrl;

}