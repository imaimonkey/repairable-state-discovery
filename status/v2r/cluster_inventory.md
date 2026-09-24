# V2R cluster inventory

2026-09-24T02:47:02.398902+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325388636160 available bytes; 81.85% used; 112498686 free inodes.

server1 `/home`: 325388636160 available bytes; 81.85% used; 112498686 free inodes.

server1 `/tmp`: 325388636160 available bytes; 81.85% used; 112498686 free inodes.

server1 `/var/tmp`: 325388636160 available bytes; 81.85% used; 112498686 free inodes.

server1 `/mnt/raid5`: 554711916544 available bytes; 97.46% used; 337733166 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40876945408 available bytes; 97.72% used; 110431418 free inodes.

server2 `/home`: 40876945408 available bytes; 97.72% used; 110431418 free inodes.

server2 `/tmp`: 40876945408 available bytes; 97.72% used; 110431418 free inodes.

server2 `/var/tmp`: 40876945408 available bytes; 97.72% used; 110431418 free inodes.

server2 `/mnt/raid5`: 528487600128 available bytes; 96.35% used; 445199000 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292670246912 available bytes; 83.67% used; 114208134 free inodes.

server3 `/home`: 292670246912 available bytes; 83.67% used; 114208134 free inodes.

server3 `/data`: 39731535872 available bytes; 99.45% used; 225845999 free inodes.

server3 `/tmp`: 292670246912 available bytes; 83.67% used; 114208134 free inodes.

server3 `/var/tmp`: 292670246912 available bytes; 83.67% used; 114208134 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106002890752 available bytes; 94.08% used; 114349825 free inodes.

server4 `/home`: 106002890752 available bytes; 94.08% used; 114349825 free inodes.

server4 `/data`: 289727152128 available bytes; 96.00% used; 225387168 free inodes.

server4 `/tmp`: 106002890752 available bytes; 94.08% used; 114349825 free inodes.

server4 `/var/tmp`: 106002890752 available bytes; 94.08% used; 114349825 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
