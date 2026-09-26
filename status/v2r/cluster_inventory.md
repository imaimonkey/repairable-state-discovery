# V2R cluster inventory

2026-09-26T01:42:59.277848+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318649094144 available bytes; 82.22% used; 112476297 free inodes.

server1 `/home`: 318649094144 available bytes; 82.22% used; 112476297 free inodes.

server1 `/tmp`: 318649094144 available bytes; 82.22% used; 112476297 free inodes.

server1 `/var/tmp`: 318649094144 available bytes; 82.22% used; 112476297 free inodes.

server1 `/mnt/raid5`: 343731646464 available bytes; 98.42% used; 337546424 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22939783168 available bytes; 98.72% used; 110406218 free inodes.

server2 `/home`: 22939783168 available bytes; 98.72% used; 110406218 free inodes.

server2 `/tmp`: 22939783168 available bytes; 98.72% used; 110406218 free inodes.

server2 `/var/tmp`: 22939783168 available bytes; 98.72% used; 110406218 free inodes.

server2 `/mnt/raid5`: 289801170944 available bytes; 98.00% used; 445055481 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84338671616 available bytes; 95.29% used; 114152364 free inodes.

server3 `/home`: 84338671616 available bytes; 95.29% used; 114152364 free inodes.

server3 `/data`: 124799774720 available bytes; 98.28% used; 225817797 free inodes.

server3 `/tmp`: 84338671616 available bytes; 95.29% used; 114152364 free inodes.

server3 `/var/tmp`: 84338671616 available bytes; 95.29% used; 114152364 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105196584960 available bytes; 94.13% used; 114346905 free inodes.

server4 `/home`: 105196584960 available bytes; 94.13% used; 114346905 free inodes.

server4 `/data`: 131392233472 available bytes; 98.18% used; 224915855 free inodes.

server4 `/tmp`: 105196584960 available bytes; 94.13% used; 114346905 free inodes.

server4 `/var/tmp`: 105196584960 available bytes; 94.13% used; 114346905 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
