# V2R cluster inventory

2026-09-26T04:24:48.013002+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318408986624 available bytes; 82.24% used; 112476272 free inodes.

server1 `/home`: 318408986624 available bytes; 82.24% used; 112476272 free inodes.

server1 `/tmp`: 318408986624 available bytes; 82.24% used; 112476272 free inodes.

server1 `/var/tmp`: 318408986624 available bytes; 82.24% used; 112476272 free inodes.

server1 `/mnt/raid5`: 330526273536 available bytes; 98.48% used; 337545477 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22933561344 available bytes; 98.72% used; 110406202 free inodes.

server2 `/home`: 22933561344 available bytes; 98.72% used; 110406202 free inodes.

server2 `/tmp`: 22933561344 available bytes; 98.72% used; 110406202 free inodes.

server2 `/var/tmp`: 22933561344 available bytes; 98.72% used; 110406202 free inodes.

server2 `/mnt/raid5`: 285645496320 available bytes; 98.03% used; 445050509 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84141015040 available bytes; 95.30% used; 114148305 free inodes.

server3 `/home`: 84141015040 available bytes; 95.30% used; 114148305 free inodes.

server3 `/data`: 124591558656 available bytes; 98.28% used; 225819617 free inodes.

server3 `/tmp`: 84141015040 available bytes; 95.30% used; 114148305 free inodes.

server3 `/var/tmp`: 84141015040 available bytes; 95.30% used; 114148305 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106002583552 available bytes; 94.08% used; 114348206 free inodes.

server4 `/home`: 106002583552 available bytes; 94.08% used; 114348206 free inodes.

server4 `/data`: 107087712256 available bytes; 98.52% used; 224929403 free inodes.

server4 `/tmp`: 106002583552 available bytes; 94.08% used; 114348206 free inodes.

server4 `/var/tmp`: 106002583552 available bytes; 94.08% used; 114348206 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
