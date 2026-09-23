# V2R cluster inventory

2026-09-23T15:51:04.082847+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41419837440 available bytes; 97.69% used; 110435193 free inodes.

server2 `/home`: 41419837440 available bytes; 97.69% used; 110435193 free inodes.

server2 `/tmp`: 41419837440 available bytes; 97.69% used; 110435193 free inodes.

server2 `/var/tmp`: 41419837440 available bytes; 97.69% used; 110435193 free inodes.

server2 `/mnt/raid5`: 550314070016 available bytes; 96.20% used; 445223261 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 376856780800 available bytes; 78.97% used; 114285296 free inodes.

server3 `/home`: 376856780800 available bytes; 78.97% used; 114285296 free inodes.

server3 `/data`: 125337137152 available bytes; 98.27% used; 225854772 free inodes.

server3 `/tmp`: 376856780800 available bytes; 78.97% used; 114285296 free inodes.

server3 `/var/tmp`: 376856780800 available bytes; 78.97% used; 114285296 free inodes.
| server4 | True | ['2', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111499276288 available bytes; 93.78% used; 114375780 free inodes.

server4 `/home`: 111499276288 available bytes; 93.78% used; 114375780 free inodes.

server4 `/data`: 37616295936 available bytes; 99.48% used; 225486703 free inodes.

server4 `/tmp`: 111499276288 available bytes; 93.78% used; 114375780 free inodes.

server4 `/var/tmp`: 111499276288 available bytes; 93.78% used; 114375780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
