# V2R cluster inventory

2026-09-25T07:20:55.138719+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318871392256 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318871392256 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318871392256 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318871392256 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 385919619072 available bytes; 98.23% used; 337558484 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22866264064 available bytes; 98.72% used; 110410498 free inodes.

server2 `/home`: 22866264064 available bytes; 98.72% used; 110410498 free inodes.

server2 `/tmp`: 22866264064 available bytes; 98.72% used; 110410498 free inodes.

server2 `/var/tmp`: 22866264064 available bytes; 98.72% used; 110410498 free inodes.

server2 `/mnt/raid5`: 343446564864 available bytes; 97.63% used; 445097645 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84446785536 available bytes; 95.29% used; 114156017 free inodes.

server3 `/home`: 84446785536 available bytes; 95.29% used; 114156017 free inodes.

server3 `/data`: 142455271424 available bytes; 98.03% used; 225812885 free inodes.

server3 `/tmp`: 84446785536 available bytes; 95.29% used; 114156017 free inodes.

server3 `/var/tmp`: 84446785536 available bytes; 95.29% used; 114156017 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638154240 available bytes; 94.11% used; 114350361 free inodes.

server4 `/home`: 105638154240 available bytes; 94.11% used; 114350361 free inodes.

server4 `/data`: 249114116096 available bytes; 96.56% used; 225015406 free inodes.

server4 `/tmp`: 105638154240 available bytes; 94.11% used; 114350361 free inodes.

server4 `/var/tmp`: 105638154240 available bytes; 94.11% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
