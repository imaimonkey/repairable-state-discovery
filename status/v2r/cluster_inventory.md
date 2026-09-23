# V2R cluster inventory

2026-09-23T21:45:54.342541+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325714272256 available bytes; 81.83% used; 112501316 free inodes.

server1 `/home`: 325714272256 available bytes; 81.83% used; 112501316 free inodes.

server1 `/tmp`: 325714272256 available bytes; 81.83% used; 112501316 free inodes.

server1 `/var/tmp`: 325714272256 available bytes; 81.83% used; 112501316 free inodes.

server1 `/mnt/raid5`: 1388126224384 available bytes; 93.63% used; 337739924 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41114103808 available bytes; 97.71% used; 110432662 free inodes.

server2 `/home`: 41114103808 available bytes; 97.71% used; 110432662 free inodes.

server2 `/tmp`: 41114103808 available bytes; 97.71% used; 110432662 free inodes.

server2 `/var/tmp`: 41114103808 available bytes; 97.71% used; 110432662 free inodes.

server2 `/mnt/raid5`: 538038710272 available bytes; 96.28% used; 445208232 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292224528384 available bytes; 83.69% used; 114170876 free inodes.

server3 `/home`: 292224528384 available bytes; 83.69% used; 114170876 free inodes.

server3 `/data`: 82483097600 available bytes; 98.86% used; 225848422 free inodes.

server3 `/tmp`: 292224528384 available bytes; 83.69% used; 114170876 free inodes.

server3 `/var/tmp`: 292224528384 available bytes; 83.69% used; 114170876 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106470141952 available bytes; 94.06% used; 114355908 free inodes.

server4 `/home`: 106470141952 available bytes; 94.06% used; 114355908 free inodes.

server4 `/data`: 300248514560 available bytes; 95.85% used; 225447835 free inodes.

server4 `/tmp`: 106470141952 available bytes; 94.06% used; 114355908 free inodes.

server4 `/var/tmp`: 106470141952 available bytes; 94.06% used; 114355908 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
