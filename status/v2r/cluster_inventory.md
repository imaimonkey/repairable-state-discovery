# V2R cluster inventory

2026-09-25T10:06:19.450219+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318835023872 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318835023872 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318835023872 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318835023872 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 368805535744 available bytes; 98.31% used; 337556983 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22826336256 available bytes; 98.73% used; 110410468 free inodes.

server2 `/home`: 22826336256 available bytes; 98.73% used; 110410468 free inodes.

server2 `/tmp`: 22826336256 available bytes; 98.73% used; 110410468 free inodes.

server2 `/var/tmp`: 22826336256 available bytes; 98.73% used; 110410468 free inodes.

server2 `/mnt/raid5`: 316336295936 available bytes; 97.81% used; 445091379 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84418396160 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84418396160 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 141877874688 available bytes; 98.04% used; 225809996 free inodes.

server3 `/tmp`: 84418396160 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84418396160 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105614204928 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614204928 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240010072064 available bytes; 96.68% used; 224990925 free inodes.

server4 `/tmp`: 105614204928 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614204928 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
