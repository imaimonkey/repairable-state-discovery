# V2R cluster inventory

2026-09-26T12:34:44.908344+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318163312640 available bytes; 82.25% used; 112474468 free inodes.

server1 `/home`: 318163312640 available bytes; 82.25% used; 112474468 free inodes.

server1 `/tmp`: 318163312640 available bytes; 82.25% used; 112474468 free inodes.

server1 `/var/tmp`: 318163312640 available bytes; 82.25% used; 112474468 free inodes.

server1 `/mnt/raid5`: 218558976000 available bytes; 99.00% used; 337537764 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19756396544 available bytes; 98.90% used; 110381972 free inodes.

server2 `/home`: 19756396544 available bytes; 98.90% used; 110381972 free inodes.

server2 `/tmp`: 19756396544 available bytes; 98.90% used; 110381972 free inodes.

server2 `/var/tmp`: 19756396544 available bytes; 98.90% used; 110381972 free inodes.

server2 `/mnt/raid5`: 240165437440 available bytes; 98.34% used; 444979688 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82650734592 available bytes; 95.39% used; 114110832 free inodes.

server3 `/home`: 82650734592 available bytes; 95.39% used; 114110832 free inodes.

server3 `/data`: 123403186176 available bytes; 98.29% used; 225823627 free inodes.

server3 `/tmp`: 82650734592 available bytes; 95.39% used; 114110832 free inodes.

server3 `/var/tmp`: 82650734592 available bytes; 95.39% used; 114110832 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105899646976 available bytes; 94.09% used; 114347942 free inodes.

server4 `/home`: 105899646976 available bytes; 94.09% used; 114347942 free inodes.

server4 `/data`: 88546566144 available bytes; 98.78% used; 224878849 free inodes.

server4 `/tmp`: 105899646976 available bytes; 94.09% used; 114347942 free inodes.

server4 `/var/tmp`: 105899646976 available bytes; 94.09% used; 114347942 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
