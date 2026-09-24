# V2R cluster inventory

2026-09-24T07:17:07.698826+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324452753408 available bytes; 81.90% used; 112491266 free inodes.

server1 `/home`: 324452753408 available bytes; 81.90% used; 112491266 free inodes.

server1 `/tmp`: 324452753408 available bytes; 81.90% used; 112491266 free inodes.

server1 `/var/tmp`: 324452753408 available bytes; 81.90% used; 112491266 free inodes.

server1 `/mnt/raid5`: 517420462080 available bytes; 97.63% used; 337722818 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57852051456 available bytes; 96.77% used; 110431133 free inodes.

server2 `/home`: 57852051456 available bytes; 96.77% used; 110431133 free inodes.

server2 `/tmp`: 57852051456 available bytes; 96.77% used; 110431133 free inodes.

server2 `/var/tmp`: 57852051456 available bytes; 96.77% used; 110431133 free inodes.

server2 `/mnt/raid5`: 518147358720 available bytes; 96.42% used; 445181461 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127137964032 available bytes; 92.91% used; 114198787 free inodes.

server3 `/home`: 127137964032 available bytes; 92.91% used; 114198787 free inodes.

server3 `/data`: 139061518336 available bytes; 98.08% used; 225834409 free inodes.

server3 `/tmp`: 127137964032 available bytes; 92.91% used; 114198787 free inodes.

server3 `/var/tmp`: 127137964032 available bytes; 92.91% used; 114198787 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105789812736 available bytes; 94.10% used; 114349211 free inodes.

server4 `/home`: 105789812736 available bytes; 94.10% used; 114349211 free inodes.

server4 `/data`: 291947851776 available bytes; 95.97% used; 225367174 free inodes.

server4 `/tmp`: 105789812736 available bytes; 94.10% used; 114349211 free inodes.

server4 `/var/tmp`: 105789812736 available bytes; 94.10% used; 114349211 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
