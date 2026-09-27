# V2R cluster inventory

2026-09-27T04:19:09.411960+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314935250944 available bytes; 82.43% used; 112443042 free inodes.

server1 `/home`: 314935250944 available bytes; 82.43% used; 112443042 free inodes.

server1 `/tmp`: 314935250944 available bytes; 82.43% used; 112443042 free inodes.

server1 `/var/tmp`: 314935250944 available bytes; 82.43% used; 112443042 free inodes.

server1 `/mnt/raid5`: 636264935424 available bytes; 97.08% used; 337400502 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17624887296 available bytes; 99.02% used; 110365008 free inodes.

server2 `/home`: 17624887296 available bytes; 99.02% used; 110365008 free inodes.

server2 `/tmp`: 17624887296 available bytes; 99.02% used; 110365008 free inodes.

server2 `/var/tmp`: 17624887296 available bytes; 99.02% used; 110365008 free inodes.

server2 `/mnt/raid5`: 577274429440 available bytes; 96.01% used; 444881751 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78699421696 available bytes; 95.61% used; 114062932 free inodes.

server3 `/home`: 78699421696 available bytes; 95.61% used; 114062932 free inodes.

server3 `/data`: 1335170777088 available bytes; 81.55% used; 225759298 free inodes.

server3 `/tmp`: 78699421696 available bytes; 95.61% used; 114062932 free inodes.

server3 `/var/tmp`: 78699421696 available bytes; 95.61% used; 114062932 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111018397696 available bytes; 93.80% used; 114372940 free inodes.

server4 `/home`: 111018397696 available bytes; 93.80% used; 114372940 free inodes.

server4 `/data`: 382149517312 available bytes; 94.72% used; 224780570 free inodes.

server4 `/tmp`: 111018397696 available bytes; 93.80% used; 114372940 free inodes.

server4 `/var/tmp`: 111018397696 available bytes; 93.80% used; 114372940 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
