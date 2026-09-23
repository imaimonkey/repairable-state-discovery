# V2R cluster inventory

2026-09-23T15:58:42.092726+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | False | [] | [] | reference_compatible=False |
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 41417199616 available bytes; 97.69% used; 110435187 free inodes.

server2 `/home`: 41417199616 available bytes; 97.69% used; 110435187 free inodes.

server2 `/tmp`: 41417199616 available bytes; 97.69% used; 110435187 free inodes.

server2 `/var/tmp`: 41417199616 available bytes; 97.69% used; 110435187 free inodes.

server2 `/mnt/raid5`: 529110827008 available bytes; 96.34% used; 445218831 free inodes.
| server3 | True | ['0'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 377018974208 available bytes; 78.96% used; 114296205 free inodes.

server3 `/home`: 377018974208 available bytes; 78.96% used; 114296205 free inodes.

server3 `/data`: 125333499904 available bytes; 98.27% used; 225854652 free inodes.

server3 `/tmp`: 377018974208 available bytes; 78.96% used; 114296205 free inodes.

server3 `/var/tmp`: 377018974208 available bytes; 78.96% used; 114296205 free inodes.
| server4 | True | ['3', '5', '6'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111499157504 available bytes; 93.78% used; 114375780 free inodes.

server4 `/home`: 111499157504 available bytes; 93.78% used; 114375780 free inodes.

server4 `/data`: 37538836480 available bytes; 99.48% used; 225486657 free inodes.

server4 `/tmp`: 111499157504 available bytes; 93.78% used; 114375780 free inodes.

server4 `/var/tmp`: 111499157504 available bytes; 93.78% used; 114375780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
