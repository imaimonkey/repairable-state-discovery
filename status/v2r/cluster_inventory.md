# V2R cluster inventory

2026-09-25T07:24:31.369467+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318871998464 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318871998464 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318871998464 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318871998464 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 385920380928 available bytes; 98.23% used; 337558472 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22860443648 available bytes; 98.72% used; 110410502 free inodes.

server2 `/home`: 22860443648 available bytes; 98.72% used; 110410502 free inodes.

server2 `/tmp`: 22860443648 available bytes; 98.72% used; 110410502 free inodes.

server2 `/var/tmp`: 22860443648 available bytes; 98.72% used; 110410502 free inodes.

server2 `/mnt/raid5`: 343404318720 available bytes; 97.63% used; 445097435 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84446556160 available bytes; 95.29% used; 114156023 free inodes.

server3 `/home`: 84446556160 available bytes; 95.29% used; 114156023 free inodes.

server3 `/data`: 142395699200 available bytes; 98.03% used; 225812787 free inodes.

server3 `/tmp`: 84446556160 available bytes; 95.29% used; 114156023 free inodes.

server3 `/var/tmp`: 84446556160 available bytes; 95.29% used; 114156023 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638055936 available bytes; 94.11% used; 114350361 free inodes.

server4 `/home`: 105638055936 available bytes; 94.11% used; 114350361 free inodes.

server4 `/data`: 249107443712 available bytes; 96.56% used; 225015046 free inodes.

server4 `/tmp`: 105638055936 available bytes; 94.11% used; 114350361 free inodes.

server4 `/var/tmp`: 105638055936 available bytes; 94.11% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
