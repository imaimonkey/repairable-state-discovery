# V2R cluster inventory

2026-09-24T02:45:27.327906+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325388611584 available bytes; 81.85% used; 112498704 free inodes.

server1 `/home`: 325388611584 available bytes; 81.85% used; 112498704 free inodes.

server1 `/tmp`: 325388611584 available bytes; 81.85% used; 112498704 free inodes.

server1 `/var/tmp`: 325388611584 available bytes; 81.85% used; 112498704 free inodes.

server1 `/mnt/raid5`: 582092038144 available bytes; 97.33% used; 337733171 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40876756992 available bytes; 97.72% used; 110431430 free inodes.

server2 `/home`: 40876756992 available bytes; 97.72% used; 110431430 free inodes.

server2 `/tmp`: 40876756992 available bytes; 97.72% used; 110431430 free inodes.

server2 `/var/tmp`: 40876756992 available bytes; 97.72% used; 110431430 free inodes.

server2 `/mnt/raid5`: 528536629248 available bytes; 96.35% used; 445199159 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292659007488 available bytes; 83.67% used; 114207553 free inodes.

server3 `/home`: 292659007488 available bytes; 83.67% used; 114207553 free inodes.

server3 `/data`: 39734349824 available bytes; 99.45% used; 225846021 free inodes.

server3 `/tmp`: 292659007488 available bytes; 83.67% used; 114207553 free inodes.

server3 `/var/tmp`: 292659007488 available bytes; 83.67% used; 114207553 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106002980864 available bytes; 94.08% used; 114349830 free inodes.

server4 `/home`: 106002980864 available bytes; 94.08% used; 114349830 free inodes.

server4 `/data`: 289728741376 available bytes; 96.00% used; 225387197 free inodes.

server4 `/tmp`: 106002980864 available bytes; 94.08% used; 114349830 free inodes.

server4 `/var/tmp`: 106002980864 available bytes; 94.08% used; 114349830 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
