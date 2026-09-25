# V2R cluster inventory

2026-09-25T11:54:53.280655+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319046168576 available bytes; 82.20% used; 112478827 free inodes.

server1 `/home`: 319046168576 available bytes; 82.20% used; 112478827 free inodes.

server1 `/tmp`: 319046168576 available bytes; 82.20% used; 112478827 free inodes.

server1 `/var/tmp`: 319046168576 available bytes; 82.20% used; 112478827 free inodes.

server1 `/mnt/raid5`: 364341522432 available bytes; 98.33% used; 337549134 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22899228672 available bytes; 98.72% used; 110409972 free inodes.

server2 `/home`: 22899228672 available bytes; 98.72% used; 110409972 free inodes.

server2 `/tmp`: 22899228672 available bytes; 98.72% used; 110409972 free inodes.

server2 `/var/tmp`: 22899228672 available bytes; 98.72% used; 110409972 free inodes.

server2 `/mnt/raid5`: 325923069952 available bytes; 97.75% used; 445081954 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84213714944 available bytes; 95.30% used; 114154982 free inodes.

server3 `/home`: 84213714944 available bytes; 95.30% used; 114154982 free inodes.

server3 `/data`: 142042177536 available bytes; 98.04% used; 225813229 free inodes.

server3 `/tmp`: 84213714944 available bytes; 95.30% used; 114154982 free inodes.

server3 `/var/tmp`: 84213714944 available bytes; 95.30% used; 114154982 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105602334720 available bytes; 94.11% used; 114350231 free inodes.

server4 `/home`: 105602334720 available bytes; 94.11% used; 114350231 free inodes.

server4 `/data`: 232573169664 available bytes; 96.79% used; 224973910 free inodes.

server4 `/tmp`: 105602334720 available bytes; 94.11% used; 114350231 free inodes.

server4 `/var/tmp`: 105602334720 available bytes; 94.11% used; 114350231 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
