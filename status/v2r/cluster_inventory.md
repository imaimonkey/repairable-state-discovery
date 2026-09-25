# V2R cluster inventory

2026-09-25T09:51:01.560767+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318837641216 available bytes; 82.21% used; 112480391 free inodes.

server1 `/home`: 318837641216 available bytes; 82.21% used; 112480391 free inodes.

server1 `/tmp`: 318837641216 available bytes; 82.21% used; 112480391 free inodes.

server1 `/var/tmp`: 318837641216 available bytes; 82.21% used; 112480391 free inodes.

server1 `/mnt/raid5`: 350844334080 available bytes; 98.39% used; 337556794 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22834360320 available bytes; 98.73% used; 110410482 free inodes.

server2 `/home`: 22834360320 available bytes; 98.73% used; 110410482 free inodes.

server2 `/tmp`: 22834360320 available bytes; 98.73% used; 110410482 free inodes.

server2 `/var/tmp`: 22834360320 available bytes; 98.73% used; 110410482 free inodes.

server2 `/mnt/raid5`: 331118587904 available bytes; 97.71% used; 445092025 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84416634880 available bytes; 95.29% used; 114156037 free inodes.

server3 `/home`: 84416634880 available bytes; 95.29% used; 114156037 free inodes.

server3 `/data`: 142295764992 available bytes; 98.03% used; 225810305 free inodes.

server3 `/tmp`: 84416634880 available bytes; 95.29% used; 114156037 free inodes.

server3 `/var/tmp`: 84416634880 available bytes; 95.29% used; 114156037 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105614659584 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614659584 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240038989824 available bytes; 96.68% used; 224992884 free inodes.

server4 `/tmp`: 105614659584 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614659584 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
