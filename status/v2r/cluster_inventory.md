# V2R cluster inventory

2026-09-23T22:33:13.704407+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325695524864 available bytes; 81.83% used; 112501389 free inodes.

server1 `/home`: 325695524864 available bytes; 81.83% used; 112501389 free inodes.

server1 `/tmp`: 325695524864 available bytes; 81.83% used; 112501389 free inodes.

server1 `/var/tmp`: 325695524864 available bytes; 81.83% used; 112501389 free inodes.

server1 `/mnt/raid5`: 1388103876608 available bytes; 93.63% used; 337739832 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41081421824 available bytes; 97.71% used; 110432627 free inodes.

server2 `/home`: 41081421824 available bytes; 97.71% used; 110432627 free inodes.

server2 `/tmp`: 41081421824 available bytes; 97.71% used; 110432627 free inodes.

server2 `/var/tmp`: 41081421824 available bytes; 97.71% used; 110432627 free inodes.

server2 `/mnt/raid5`: 536553721856 available bytes; 96.29% used; 445206636 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293025980416 available bytes; 83.65% used; 114223205 free inodes.

server3 `/home`: 293025980416 available bytes; 83.65% used; 114223205 free inodes.

server3 `/data`: 82429730816 available bytes; 98.86% used; 225847316 free inodes.

server3 `/tmp`: 293025980416 available bytes; 83.65% used; 114223205 free inodes.

server3 `/var/tmp`: 293025980416 available bytes; 83.65% used; 114223205 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106366410752 available bytes; 94.06% used; 114354423 free inodes.

server4 `/home`: 106366410752 available bytes; 94.06% used; 114354423 free inodes.

server4 `/data`: 300065632256 available bytes; 95.85% used; 225436616 free inodes.

server4 `/tmp`: 106366410752 available bytes; 94.06% used; 114354423 free inodes.

server4 `/var/tmp`: 106366410752 available bytes; 94.06% used; 114354423 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
