# V2R cluster inventory

2026-09-25T12:05:34.836046+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319129120768 available bytes; 82.20% used; 112478316 free inodes.

server1 `/home`: 319129120768 available bytes; 82.20% used; 112478316 free inodes.

server1 `/tmp`: 319129120768 available bytes; 82.20% used; 112478316 free inodes.

server1 `/var/tmp`: 319129120768 available bytes; 82.20% used; 112478316 free inodes.

server1 `/mnt/raid5`: 364367699968 available bytes; 98.33% used; 337548569 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22910959616 available bytes; 98.72% used; 110409968 free inodes.

server2 `/home`: 22910959616 available bytes; 98.72% used; 110409968 free inodes.

server2 `/tmp`: 22910959616 available bytes; 98.72% used; 110409968 free inodes.

server2 `/var/tmp`: 22910959616 available bytes; 98.72% used; 110409968 free inodes.

server2 `/mnt/raid5`: 325853507584 available bytes; 97.75% used; 445081862 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84212404224 available bytes; 95.30% used; 114154982 free inodes.

server3 `/home`: 84212404224 available bytes; 95.30% used; 114154982 free inodes.

server3 `/data`: 142123737088 available bytes; 98.04% used; 225812545 free inodes.

server3 `/tmp`: 84212404224 available bytes; 95.30% used; 114154982 free inodes.

server3 `/var/tmp`: 84212404224 available bytes; 95.30% used; 114154982 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105378414592 available bytes; 94.12% used; 114350232 free inodes.

server4 `/home`: 105378414592 available bytes; 94.12% used; 114350232 free inodes.

server4 `/data`: 232502382592 available bytes; 96.79% used; 224971307 free inodes.

server4 `/tmp`: 105378414592 available bytes; 94.12% used; 114350232 free inodes.

server4 `/var/tmp`: 105378414592 available bytes; 94.12% used; 114350232 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
